import React from "react";
import styled from "styled-components";
import {Header} from "./header";
import {RadioButtons} from "./RadioButtons";
import { AnswerInput } from "./answerInput";
import {AnswerButton} from "./answerButton";
import {formToJSON} from "axios";
import {handleSurveyPost} from "../api/endApi";


const StyledSurvey = styled.form`
position: absolute;
  right: 20px;
  top: 20px;
  min-width: 350px;
  min-height: 680px;
  padding: 10px;
  border: 2px dashed black;
  margin-bottom: 10px;
`



export const Survey = ({userId}) => {

  const [gender, setGender] = React.useState()
  const [edu, setEdu] = React.useState()
  const [age, setAge] = React.useState()

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = {age: age, education: edu, gender: gender}
    handleSurveyPost(userId, data)
  }

  return(
      <StyledSurvey id={'sur'}>
        <p>
          Want to help us? Answer this 3 min survey!
        </p>
        <p>
          Gender:
        </p>
        <RadioButtons data={['Male', 'Female', 'Other / Prefer not to say']} name={'gender'} handler={setGender}/>
        <p>
          Education:
        </p>
        <RadioButtons data={['Undergrad', 'Bachelor', 'Master']} name={'education'} handler={setEdu}/>
        <p>
          Age:
        </p>
        <RadioButtons data={['18-25', '26-32', '33-40', '41-50', '51-60', '60+']} name={'age'} smol={true} handler={setAge}/>
        <AnswerButton onClick={handleSubmit} />
      </StyledSurvey>
  )
}