import React from "react";
import styled from "styled-components";
import {Header} from "./header";
import {RadioButtons} from "./RadioButtons";
import { AnswerInput } from "./answerInput";
import {AnswerButton} from "./answerButton";


const StyledSurvey = styled.form`
position: absolute;
  right: 50px;
  top: 50px;
  width: 350px;
  height: 630px;
  padding: 20px;
  border: 2px dashed black;
  margin-bottom: 10px;
`



export const Survey = () => {

  return(
      <StyledSurvey>
        <p>
          Want to help us? Answer this 3 min survey!
        </p>
        <p>
          Gender:
        </p>
        <RadioButtons data={['Male', 'Female', 'Other / Prefer not to say']} name={'gender'}/>
        <p>
          Education:
        </p>
        <RadioButtons data={['Undergrad', 'Bachelor', 'Master']} name={'education'}/>
        <p>
          Age:
        </p>
        <RadioButtons data={['18-25', '26-32', '33-40', '41-50', '51-60', '60+']} name={'age'} smol={true}/>
      </StyledSurvey>
  )
}