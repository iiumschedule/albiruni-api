import pandas as pd

def find_exam(subject_code: str, session: str, semester: int):
    exam_date = ''
    exam_time = ''
    found_exam = False

    # read the Excel file
    try:
        df = pd.read_excel(f'db/exams/{session}/Sem{semester}.xlsx', sheet_name='Page001')
    except FileNotFoundError:
        raise Exception('Examination schedule not available')

    for i in range(len(df.columns)):
        # print(f'iteration {i}')
        values = df.iloc[:, i]

        if not pd.isna(values[0]):
            exam_date = values[0]

        exam_time = values[1]

        if subject_code in values.values:
            found_exam = True
            break

    if not found_exam:
        raise Exception('Exam not found')

    return exam_date, exam_time
