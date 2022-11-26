import React from 'react';
import { useParams } from "react-router-dom";
import { Header } from "../components/header";
import { PageWrapper } from "../utils/PageWrapper";
import {Task} from "../components/task";
import { AnswerInput } from "../components/answerInput";
import { AnswerButton } from "../components/answerButton";
import { InfoBox } from "../components/infoBox";
import { Navigate } from "react-router-dom";

import styled from "styled-components";
import {handleTaskCheck, handleTaskGet} from "../api/taskApi";
import {ErrorPage} from "../components/errorPage";


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
  const [data, setData] = React.useState(null)
  const [result, setResult] = React.useState(1)


  React.useEffect(() => {
    data === null && handleTaskGet(setData, userId)
  })

  const handleChange = (event) => {
    setAns(event.target.value);
  }

  const handleSubmitAnswer = async () => {
    await handleTaskCheck(ans, userId, setResult)
    document.location.reload()
  }
  if (data === null)
    return(
        <div />
    )


  if (data === 'ERROR')
    return(
        <ErrorPage />
    )


  if (data.try_num > data.max_tries)
    return(
        <Navigate to={`/fail`} />
    )


  if (data.is_finished)
    return (
        <Navigate to={`/result/${userId}`} />
    )

    return(
        <PageWrapper>
          <Header title={data.title} />
          <InfoBox attemptNumber={data.try_num} maxAttempts={data.max_tries} taskNumber={data.task_number} maxTasks={data.max_task_number}/>
          <Task content = {data.task}/>

          <AnswerContainer>
            <AnswerInput onChange = {handleChange} />
            <AnswerButton onClick={handleSubmitAnswer} />
          </AnswerContainer>
        </PageWrapper>
    )

}