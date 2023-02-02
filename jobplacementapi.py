import pickle
import  streamlit as st

model= pickle.load(open('C:/Users/Honour Jesus/Downloads/job-placement,pkl','rb'))

def main():
    st.title('Job Placement Predictions')

    #input variables
    Gender= st.text_input('Gender')
    Degree= st.text_input('undergrad_degree')
    Work_Experience= st.text_input('work_experience')
    Specialisation= st.text_input('specialisation')
    Mba_Score= st.text_input('mba_percent')
    Degree_Percentage= st.text_input('degree_percentage')

    #prediction
    if st.button('predict'):
        makeprediction = model.predict([[Gender,Degree,Work_Experience,Specialisation,Mba_Score,Degree_Percentage]])
        output=round(makeprediction[0],2)
        st.success('You got the job {}'.format(output))

if __name__=='__main__':   
    main()     