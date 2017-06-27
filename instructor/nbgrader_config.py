from nbgrader.utils import get_username

c = get_config()

c.NbGrader.course_id = "KJM1101"
c.NbGrader.db_assignments = [dict(name="lab1")]
c.NbGrader.db_students = [dict(id=get_username())]

c.ClearSolutions.code_stub = {"python": "# SKRIV DITT SVAR HER\nraise NotImplementedError"}

