import React from "react";
import styled from "styled-components";
import {PageWrapper} from "../utils/PageWrapper";
import {Header} from "../components/header";
import {Task} from "../components/task";



export const FailPage = () => {
  return(
      <PageWrapper>
        <Header title={'Sorry!'} />
        <Task content={"Unfortunately, you failed to complete the Challenge. You can try again from the beggining, it's really worth it"} />
      </PageWrapper>
  )
}