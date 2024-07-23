from neo4j import GraphDatabase

def consulta_1(driver):
    with driver.session() as session:
        result = session.run(
            """
            MATCH (s:Salary)
            RETURN s.experience_level AS experience_level, avg(s.salary_in_usd) AS average_salary
            """
        )
        for record in result:
            print(f"experience_level: {record['experience_level']}, average_salary: {record['average_salary']}")

def consulta_2(driver):
    with driver.session() as session:
        result = session.run(
            """
            MATCH (s:Salary)
            RETURN s.company_location AS company_location, s.experience_level AS experience_level, avg(s.salary_in_usd) AS average_salary
            ORDER BY average_salary DESC
            """
        )
        for record in result:
            print(f"company_location: {record['company_location']}, experience_level: {record['experience_level']}, average_salary: {record['average_salary']}")

def consulta_3(driver):
    with driver.session() as session:
        result = session.run(
            """
            MATCH (s:Salary)
            RETURN s.company_location AS company_location, avg(s.salary_in_usd) AS average_salary
            ORDER BY average_salary DESC
            """
        )
        for record in result:
            print(f"company_location: {record['company_location']}, average_salary: {record['average_salary']}")

def consulta_4(driver):
    with driver.session() as session:
        result = session.run(
            """
            MATCH (s:Salary)
            RETURN avg(s.salary_in_usd) AS average_salary
            """
        )
        for record in result:
            print(f"average_salary: {record['average_salary']}")

def consulta_5(driver):
    with driver.session() as session:
        result = session.run(
            """
            MATCH (s:Salary)
            RETURN s.job_title AS job_title, avg(s.salary_in_usd) AS average_salary
            ORDER BY average_salary DESC
            """
        )
        for record in result:
            print(f"job_title: {record['job_title']}, average_salary: {record['average_salary']}")

def menu():
    uri = "neo4j://localhost:7687"
    user = "neo4j"
    password = "joaquin123"  # Reemplaza con tu contraseña de Neo4j
    driver = GraphDatabase.driver(uri, auth=(user, password))

    while True:
        print("\nMenú de Consultas de Salarios")
        print("1. Diferencia de salario entre los niveles de desarrolladores")
        print("2. Lugares con mayor salario según nivel de experiencia")
        print("3. ¿USA es el país con mejores salarios?")
        print("4. Salario promedio global")
        print("5. Área informática con mayor sueldo")
        print("6. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 6:
            print("Saliendo...")
            break
        elif opcion == 1:
            consulta_1(driver)
        elif opcion == 2:
            consulta_2(driver)
        elif opcion == 3:
            consulta_3(driver)
        elif opcion == 4:
            consulta_4(driver)
        elif opcion == 5:
            consulta_5(driver)
        else:
            print("Opción no válida, por favor seleccione una opción válida.")

    driver.close()

if __name__ == "__main__":
    menu()
