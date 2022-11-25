import React from 'react';
import { useParams } from "react-router-dom";
import {PageWrapper} from "../utils/PageWrapper";
import {Header} from "../components/header";
import {Task} from "../components/task";


export const EndPage = () => {


  const prompt = 'You finished zadanka and taski';
  const userId = useParams().id;
  return(
      <PageWrapper>
        <Header title={'Congratulations!'} />
        <Task content={prompt + ' ' + userId} />
      </PageWrapper>
  )
}