import React from 'react';
import { useParams } from "react-router-dom";
import { Header } from "../components/header";
import { PageWrapper } from "../utils/PageWrapper";
import {Task} from "../components/task";
import { AnswerInput } from "../components/answerInput";
import { AnswerButton } from "../components/answerButton";
import { InfoBox } from "../components/infoBox";

import styled from "styled-components";


const mockQuestion = 'ile w wodociągach wody jest? Odpowiedz uzasadnij';

const AnswerContainer = styled.div`
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  width: 500px;
  margin-top: 50px;
`

export const TaskPage = () => {
  const userId = useParams().id
  const [ans, setAns] = React.useState()

  const handleChange = (event) => {
    setAns(event.target.value);
  }

  const handleSubmitAnswer = () => {
    console.log(ans);
  }

  return(
      <PageWrapper>
        <Header title={'Wodociagi question 1'} />
        <InfoBox attemptNumber={2} maxAttempts={7} taskNumber={3} maxTasks={5}/>
        <Task content = {mockQuestion + '  ' + userId}/>

        <AnswerContainer>
          <AnswerInput onChange = {handleChange} />
          <AnswerButton onClick={handleSubmitAnswer} />
        </AnswerContainer>
      </PageWrapper>
  )
}