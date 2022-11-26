import React from 'react';
import { useParams } from "react-router-dom";
import {PageWrapper} from "../utils/PageWrapper";
import {Header} from "../components/header";
import {Task} from "../components/task";
import {handleEndGet} from "../api/endApi";
import {ErrorPage} from "../components/errorPage";


export const EndPage = () => {
  const [data, setData] = React.useState(null)
  const userId = useParams().id

  React.useEffect(() => {
    data === null && handleEndGet(setData, userId)
  })

  const prompt = 'You finished zadanka and taski';
  if (data === 'error')
    return(
        <ErrorPage />
    )

  if (data !== null)
  return(
      <PageWrapper>
        <Header title={'Congratulations!'} />
        <Task content={data} />
      </PageWrapper>
  )

  return(
      <div />
  )
}