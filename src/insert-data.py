import pandas as pd
from neo4j import GraphDatabase

# Función para insertar datos en Neo4j
def insertar_datos():
    file_path = 'dataset-salary.csv'  # Asegúrate de que esta ruta es correcta
    data = pd.read_csv(file_path)
    
    uri = "neo4j://localhost:7687"  # URI de conexión local
    user = "neo4j"
    password = "##"  # Reemplaza con tu contraseña de Neo4j
    driver = GraphDatabase.driver(uri, auth=(user, password))
    
    try:
        with driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")  # Limpiar la base de datos
        
            for index, row in data.iterrows():
                session.run(
                    """
                    CREATE (:Salary {
                        work_year: $work_year,
                        experience_level: $experience_level,
                        employment_type: $employment_type,
                        job_title: $job_title,
                        salary: $salary,
                        salary_currency: $salary_currency,
                        salary_in_usd: $salary_in_usd,
                        employee_residence: $employee_residence,
                        remote_ratio: $remote_ratio,
                        company_location: $company_location,
                        company_size: $company_size
                    })
                    """,
                    {
                        "work_year": row["work_year"],
                        "experience_level": row["experience_level"],
                        "employment_type": row["employment_type"],
                        "job_title": row["job_title"],
                        "salary": row["salary"],
                        "salary_currency": row["salary_currency"],
                        "salary_in_usd": row["salary_in_usd"],
                        "employee_residence": row["employee_residence"],
                        "remote_ratio": row["remote_ratio"],
                        "company_location": row["company_location"],
                        "company_size": row["company_size"],
                    }
                )
        print("Datos insertados correctamente en Neo4j")
    except Exception as e:
        print(f"Error al insertar los datos: {e}")
    finally:
        driver.close()

if __name__ == "__main__":
    insertar_datos()
