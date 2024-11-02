import streamlit as st

# Define the credit and grade functions and dictionaries as before
def getcredits(Branch, semester):
    if Branch == 1:
        return CSBS[semester-1]
    elif Branch == 2:
        return CSD[semester - 1]
    elif Branch == 3:
        return CSE[semester - 1]
    elif Branch == 4:
        return CSM[semester - 1]
    elif Branch == 5:
        return CSO[semester - 1]
    elif Branch == 6:
        return IT[semester - 1]
    elif Branch == 7:
        return ECE[semester - 1]
    elif Branch == 8:
        return EEE[semester - 1]
    elif Branch == 9:
        return CHE[semester - 1]
    elif Branch == 10:
        return CIVIL[semester - 1]
    elif Branch == 11:
        return ME[semester - 1]
    else:
        st.error("Invalid Branch or Semester")
        return None

def grade(g):
    grade_map = {'A+': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 0}
    return grade_map.get(g, None)

# Credits data as per Branch and Semester
CSBS=[[[3,3,3,3,3],[1,1,1,1.5]],[[3,3,3,3,3],[1,1,1,1.5]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,2,1.5,2]],[[2,3,3,3,3,3],[1,1,2]],[[2,3,3,3,3,3],[1,3,2]],[[],[12]]]


CSM=[[[3,3,3,3],[1.5,1.5,3,1.5]],[[3,3,3,3,2],[1.5,1.5,1.5,1]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3,3],[3,2]],[[],[12]]]


CSE=[[[3,3,3,3],[1.5,1.5,3,1.5]],[[3,3,3,3,2],[1.5,1,1.5,1.5]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3,3],[3,2]],[[],[12]]]


CHE=[[[3,3,3,3],[1.5,1.5,1.5,3]],[[3,3,3,3],[1.5,1.5,1.5,3]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,2]],[[3,3,3,3,3,3],[3,1.5,2]],[[],[12]]]


CIVIL=[[[3,3,3,3],[1.5,1.5,3,1.5]],[[3,3,3,3],[1.5,1.5,3,1.5]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3,3],[3,2]],[[],[12]]]


CSD=[[[3,3,3,3],[1.5,1.5,3,1.5]],[[3,3,3,3,2],[1.5,1,1.5,1.5]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3,3],[3,2]],[[],[12]]]


CSO=[[[3,3,3,3],[1.5,1.5,3,1.5]],[[3,3,3,3,2],[1.5,1,1.5,1.5]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3,3],[3,2]],[[],[12]]]


ECE=[[[3,3,3,3],[1.5,1,3,2]],[[3,3,3,3],[1.5,2,3,1]],[[3,4,3,3,3],[1,1.5,1,2]],[[3,3,4,3,3],[1.5,1,1,2]],[[3,3,3,3,3],[1.5,2,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1,2]],[[3,3,3,3,3,3],[3,2]],[[],[12]]]


EEE=[[[3,3,3,3],[1.5,1.5,3,1.5]],[[3,3,3,3],[1.5,1.5,3,1.5]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[2,3,3,3,3],[3,1.5,1,2]],[[3,3,3,3,3,3],[3,2]],[[],[12]]]


IT=[[[3,3,3,3],[1.5,1.5,3,1.5]],[[3,3,3,3,2],[1.5,1,1.5,1.5]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3,3],[3,2]],[[],[12]]]


ME=[[[3,3,3,3],[1.5,1.5,3,1.5]],[[3,3,3,3,3],[1.5,1.5,1.5]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3],[1.5,1.5,1.5,2]],[[3,3,3,3,3,3],[3,2]],[[],[12]]]


# Streamlit Frontend
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 40px;
        color: #f4d03f;
        font-family: Arial, sans-serif;
    }
    </style>
    <h1 class="title">RVR SGPA Calculator</h1>
    """,
    unsafe_allow_html=True
)

# Branch and Semester input
branch_name = st.selectbox("Select Branch", ("CSBS", "CSD", "CSE", "CHE", "CIVIL", "CSM", "CSO", "ECE", "EEE", "IT", "ME"))
semester = st.number_input("Enter Semester", min_value=1, max_value=8)

# Mapping branch name to corresponding integer
branch_map = {
    "CSBS": 1, "CSD": 2, "CSE": 3, "CHE": 9, "CIVIL": 10, "CSM": 4, "CSO": 5, "ECE": 7, "EEE": 8, "IT": 6, "ME": 11
}
branch = branch_map[branch_name]

# Get credits based on Branch and Semester
semcredits = getcredits(branch, semester)
if semcredits:
    # Input subject grades
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h1 style="color: #f5b041; font-size: 36px;">Enter Grades for Subjects</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    sub_grades = []
    for i in range(len(semcredits[0])):
        grade_input = st.selectbox(f"Subject {i + 1} Grade", ("A+", "A", "B", "C", "D", "E", "F"))
        sub_grades.append(grade(grade_input))
    
    # Input lab grades
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h1 style="color: #f5b041; font-size: 36px;">Enter Grades for Labs</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    lab_grades = []
    for i in range(len(semcredits[1])):
        grade_input = st.selectbox(f"Lab {i + 1} Grade", ("A+", "A", "B", "C", "D", "E", "F"))
        lab_grades.append(grade(grade_input))
    
    # Calculate GPA
    gp = 0
    t = 0
    for i in range(len(semcredits[0])):
        gp += sub_grades[i] * semcredits[0][i]
        t += semcredits[0][i]
    for i in range(len(semcredits[1])):
        gp += lab_grades[i] * semcredits[1][i]
        t += semcredits[1][i]
    
    # Display GPA
    gpa = gp / t if t != 0 else 0
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h1 style="color: #4CAF50; font-size: 36px;">Your GPA is: {gpa:.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
