"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd # type: ignore
import os

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
     # Read the CSV file
    df = pd.read_csv("./files/input/solicitudes_de_credito.csv", sep=";", index_col=0)
    
    # Clean text columns
    df[["sexo", "tipo_de_emprendimiento"]] = df[["sexo", "tipo_de_emprendimiento"]].apply(lambda col: col.str.lower())

    for col in ["idea_negocio", "barrio", "línea_credito"]:
        df[col] = df[col].str.lower().replace(r"[-_]", " ", regex=True)
    
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(".00", "", regex=False).replace(r"[,. $]", "", regex=True)

    # format fecha_de_beneficio as "%Y/%m/%d"
    df['fecha_de_beneficio'] = pd.to_datetime(
        df['fecha_de_beneficio'],
        format='mixed',
        dayfirst=True
    )
    
    # Remove missing values and duplicates
    df = df.dropna().drop_duplicates()
    
    # Create output directory and save file
    outputPath = "./files/output"
    
    os.makedirs(outputPath, exist_ok=True)
    df.to_csv(os.path.join(outputPath, "solicitudes_de_credito.csv"), sep=";", index=False)