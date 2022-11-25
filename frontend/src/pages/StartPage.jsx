import React from 'react';
import {PageWrapper} from "../utils/PageWrapper";
import {useParams} from "react-router-dom";
import {Header} from "../components/header";
import {Task} from "../components/task";



export const StartPage = () => {


  const prompt = 'This is a mock start page. Maybe nobody will ever see it. Or maybe they will. Idk. Depends on our time management and task completions :)';
  return(
      <PageWrapper>
        <Header title={'Hello hackathon world!'} />
        <Task content={prompt} />
      </PageWrapper>
  )
}