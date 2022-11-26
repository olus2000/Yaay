import React from 'react';
import {PageWrapper} from "../utils/PageWrapper";
import {useParams} from "react-router-dom";
import {Header} from "../components/header";
import {Task} from "../components/task";
import {handleStartGet} from "../api/startApi";
import { Navigate } from "react-router-dom";


export const StartPage = () => {
  const eventId = useParams().eventId
  const [token, setToken] = React.useState(null);
  console.log(token)

  React.useEffect(() => {
    token === null && handleStartGet(setToken, eventId);
  })
  const prompt = 'This is a mock start page. Maybe nobody will ever see it. Or maybe they will. Idk. Depends on our time management and task completions :)';
  const errorPrompt = "This event does not exist. It probably finished, didn't start, or wasn't even planned."

  if (token === 'wrong event')
    return(
        <PageWrapper>
          <Header title={'I do not exist!'} />
          <Task content={errorPrompt} />
        </PageWrapper>
    )

  if(token !== null)
  return(
      <PageWrapper>
        <Header title={'Hello hackathon world!'} />
        <Task content={prompt} />
        <Navigate to={`/task/${token}`}/>
      </PageWrapper>
  )

  return(
      <div />
  )
}