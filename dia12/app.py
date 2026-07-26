import streamlit as st
import pandas as pd
from datetime import date

ARCHIVO_DATOS = "transacciones.csv"
categorias = ["Alimentación", "Transporte", "Entretenimiento", "Salud", "Educación", "Otros"]


class Transaccion:
    """Representa una transacción individual de ingreso o gasto."""

    def __init__(self, descripcion, monto, fecha, categoria, tipo):
        self.descripcion = descripcion
        self.monto = float(monto)
        self.fecha = fecha
        self.categoria = categoria
        self.tipo = tipo

    def to_dict(self):
        """Convierte la transacción a un diccionario."""
        return {
            "descripcion": self.descripcion,
            "monto": self.monto,
            "fecha": self.fecha,
            "categoria": self.categoria,
            "tipo": self.tipo
        }

    @classmethod
    def from_dict(cls, datos):
        """Construye una Transaccion a partir de un diccionario."""
        return cls(
            descripcion=datos["descripcion"],
            monto=datos["monto"],
            fecha=datos["fecha"],
            categoria=datos["categoria"],
            tipo=datos["tipo"]
        )


class GestorTransacciones:
    """Contiene toda la lógica de negocio sobre las transacciones, sin código de Streamlit."""

    def __init__(self):
        self.transacciones = []

    def cargar(self):
        """Lee ARCHIVO_DATOS y carga las transacciones, o deja la lista vacía si falla la lectura."""
        try:
            df_datos = pd.read_csv(ARCHIVO_DATOS)
        except Exception:
            self.transacciones = []
            return

        transacciones = []
        for _, fila in df_datos.iterrows():
            transacciones.append(Transaccion(
                descripcion=fila["descripcion"],
                monto=float(fila["monto"]),
                fecha=date.fromisoformat(str(fila["fecha"])),
                categoria=fila["categoria"],
                tipo=fila["tipo"]
            ))
        self.transacciones = transacciones

    def guardar(self):
        """Escribe las transacciones actuales en ARCHIVO_DATOS en formato CSV."""
        df_datos = pd.DataFrame([t.to_dict() for t in self.transacciones])
        df_datos.to_csv(ARCHIVO_DATOS, index=False)

    def agregar(self, transaccion):
        """Agrega una Transaccion a la lista."""
        self.transacciones.append(transaccion)

    def filtrar(self, categorias_seleccionadas, fecha_desde, fecha_hasta):
        """Devuelve una lista nueva de Transaccion cuya categoría y fecha coinciden con los filtros elegidos."""
        transacciones_filtradas = []
        for t in self.transacciones:
            if t.categoria in categorias_seleccionadas and fecha_desde <= t.fecha <= fecha_hasta:
                transacciones_filtradas.append(t)
        return transacciones_filtradas

    def calcular_resumen(self, transacciones):
        """Calcula ingresos, gastos, balance y gasto promedio de una lista de transacciones."""
        ingresos = sum(t.monto for t in transacciones if t.tipo == "Ingreso")
        montos_gastos = [t.monto for t in transacciones if t.tipo == "Gasto"]
        gastos = sum(montos_gastos)
        balance = ingresos - gastos
        gasto_promedio = gastos / len(montos_gastos) if montos_gastos else 0
        return ingresos, gastos, balance, gasto_promedio

    def calcular_totales_por_categoria(self, transacciones):
        """Agrupa (con Python puro) el total de gastos por categoría."""
        gastos = [t for t in transacciones if t.tipo == "Gasto"]
        total_por_categoria = {}
        for t in gastos:
            total_por_categoria[t.categoria] = total_por_categoria.get(t.categoria, 0) + t.monto
        return total_por_categoria

    def calcular_totales_por_fecha(self, transacciones):
        """Agrupa (con Python puro) el total de gastos por fecha, para luego ordenarlos cronológicamente."""
        gastos = [t for t in transacciones if t.tipo == "Gasto"]
        total_por_fecha = {}
        for t in gastos:
            total_por_fecha[t.fecha] = total_por_fecha.get(t.fecha, 0) + t.monto
        return total_por_fecha

    def importar_desde_csv(self, archivo):
        """Lee, valida y convierte un CSV en Transacciones, devolviendo un resumen del resultado."""
        columnas_esperadas = ["descripcion", "monto", "fecha", "categoria", "tipo"]

        try:
            df_csv = pd.read_csv(archivo)
        except Exception:
            return {"error": "csv_invalido"}

        columnas_faltantes = [columna for columna in columnas_esperadas if columna not in df_csv.columns]
        if columnas_faltantes:
            return {"error": "columnas_faltantes", "columnas_esperadas": columnas_esperadas}

        importadas = 0
        con_error = 0

        for _, fila in df_csv.iterrows():
            try:
                transaccion = Transaccion(
                    descripcion=fila["descripcion"],
                    monto=float(fila["monto"]),
                    fecha=date.fromisoformat(str(fila["fecha"])),
                    categoria=fila["categoria"],
                    tipo=fila["tipo"]
                )
            except (ValueError, TypeError):
                con_error += 1
                continue

            self.agregar(transaccion)
            importadas += 1

        return {"error": None, "importadas": importadas, "con_error": con_error}


class AppFinanzas:
    """Maneja toda la interfaz de Streamlit y coordina un GestorTransacciones."""

    def inicializar_estado(self):
        """Crea el GestorTransacciones en session_state la primera vez, cargándolo desde disco."""
        if "gestor" not in st.session_state:
            gestor = GestorTransacciones()
            gestor.cargar()
            st.session_state.gestor = gestor
        self.gestor = st.session_state.gestor

    def mostrar_titulos(self):
        """Muestra el título, la descripción y la versión de la app."""
        st.title("Control de Finanzas personales")
        st.write("LLeva un control de tus gastos e ingresos de manera sencilla y rápida.")
        st.caption("Version 1.0")

    def mostrar_formulario(self):
        """Muestra el formulario de carga y, al enviarse, agrega la transacción al estado."""
        with st.form("formulario_transaccion"):
            descripcion = st.text_input("Describe tu ingreso o gasto:", placeholder="Ejemplo: Compra de comida")
            monto = st.number_input("Monto:", step=1.0, min_value=0.0, format="%.2f")
            fecha = st.date_input("Fecha:")
            tipo = st.radio("Tipo:", ["Ingreso", "Gasto"], horizontal=True)
            categoria = st.selectbox("Categoría:", categorias)
            enviado = st.form_submit_button("Guardar")

        if enviado:
            self.gestor.agregar(Transaccion(descripcion, monto, fecha, categoria, tipo))
            st.toast("Transacción guardada exitosamente.")

    def mostrar_transacciones(self, transacciones):
        """Muestra el subheader y las transacciones registradas, o un mensaje si no hay ninguna."""
        if transacciones:
            df_transacciones = pd.DataFrame([t.to_dict() for t in transacciones])
            st.subheader("Transacciones registradas:")
            st.dataframe(df_transacciones)

            csv_transacciones = df_transacciones.to_csv(index=False)
            st.download_button(
                "Descargar transacciones",
                data=csv_transacciones,
                file_name="mis_transacciones.csv",
                mime="text/csv"
            )

        else:
            st.info("No hay transacciones registradas aún.")

    def mostrar_resumen(self, transacciones):
        """Calcula ingresos, gastos, balance y gasto promedio, y los muestra como métricas."""
        if not transacciones:
            st.info("No hay transacciones registradas aún.")
            return

        ingresos, gastos, balance, gasto_promedio = self.gestor.calcular_resumen(transacciones)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Ingresos", f"${ingresos:.2f}")
        col2.metric("Gastos", f"${gastos:.2f}")
        col3.metric("Balance", f"${balance:.2f}")
        col4.metric("Gasto promedio", f"${gasto_promedio:.2f}")

    def mostrar_analisis(self, transacciones):
        """Agrupa los gastos por categoría y por fecha, y los grafica."""
        gastos = [t for t in transacciones if t.tipo == "Gasto"]

        if not gastos:
            st.info("No hay gastos registrados aún.")
            return

        total_por_categoria = self.gestor.calcular_totales_por_categoria(transacciones)
        total_por_fecha = self.gestor.calcular_totales_por_fecha(transacciones)
        fechas_ordenadas = sorted(total_por_fecha.keys())

        st.subheader("Gastos por categoría")
        df_categoria = pd.DataFrame(
            list(total_por_categoria.items()), columns=["Categoria", "Total"]
        )
        st.bar_chart(df_categoria, x="Categoria", y="Total")

        st.subheader("Gastos por fecha")
        df_fecha = pd.DataFrame({
            "Fecha": fechas_ordenadas,
            "Total": [total_por_fecha[fecha] for fecha in fechas_ordenadas]
        })
        st.line_chart(df_fecha, x="Fecha", y="Total")

    def mostrar_filtros(self):
        """Muestra los widgets de filtro (categorías y rango de fechas) y devuelve los valores elegidos."""
        if self.gestor.transacciones:
            fechas = [t.fecha for t in self.gestor.transacciones]
            fecha_min = min(fechas)
            fecha_max = max(fechas)
        else:
            fecha_min = date.today()
            fecha_max = date.today()

        categorias_seleccionadas = st.multiselect("Categorías", categorias, default=categorias)
        fecha_desde = st.date_input("Desde", value=fecha_min)
        fecha_hasta = st.date_input("Hasta", value=fecha_max)

        return categorias_seleccionadas, fecha_desde, fecha_hasta

    def importar_csv(self):
        """Muestra el expander de importación de CSV y los mensajes según el resultado de la importación."""
        with st.expander("Importar desde CSV"):
            archivo = st.file_uploader("Subí un archivo CSV", type="csv")
            importar = st.button("Importar Transacciones")

            if not importar:
                return

            if archivo is None:
                st.warning("Primero subí un archivo CSV.")
                return

            resultado = self.gestor.importar_desde_csv(archivo)

            if resultado["error"] == "csv_invalido":
                st.error("El archivo no es un CSV válido.")
                return

            if resultado["error"] == "columnas_faltantes":
                st.error(f"Faltan columnas en el CSV. Se esperan: {', '.join(resultado['columnas_esperadas'])}")
                return

            if resultado["con_error"]:
                st.warning(f"{resultado['con_error']} fila(s) no se pudieron importar.")

            if resultado["importadas"]:
                st.success(f"Se importaron {resultado['importadas']} transacción(es).")

    def run(self):
        """Organiza el flujo principal: inicializa el estado, arma el sidebar, las pestañas, y guarda al final."""
        self.mostrar_titulos()
        self.inicializar_estado()

        # El formulario de carga, la importación de CSV y los filtros se muestran en la barra lateral
        with st.sidebar:
            self.mostrar_formulario()
            self.importar_csv()
            categorias_seleccionadas, fecha_desde, fecha_hasta = self.mostrar_filtros()

        transacciones_filtradas = self.gestor.filtrar(categorias_seleccionadas, fecha_desde, fecha_hasta)

        tab_resumen, tab_movimientos, tab_analisis = st.tabs(["Resumen", "Movimientos", "Análisis"])

        # Pestaña de resumen: dashboard de métricas de ingresos, gastos, balance y gasto promedio
        with tab_resumen:
            self.mostrar_resumen(transacciones_filtradas)

        # Pestaña de movimientos: lista las transacciones registradas
        with tab_movimientos:
            self.mostrar_transacciones(transacciones_filtradas)

        # Pestaña de análisis: gráficos de gastos por categoría y por fecha
        with tab_analisis:
            self.mostrar_analisis(transacciones_filtradas)

        self.gestor.guardar()


app = AppFinanzas()
app.run()
