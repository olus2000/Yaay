import React from "react";
import styled from "styled-components";
import { PageWrapper } from "../utils/PageWrapper";
import {Header} from "./header";
import {Task} from "./task";


export const ErrorPage = () => {
  return (
      <PageWrapper>
        <Header title={'This page does not exist!'}/>
        <Task content={"Don't try and cheat around the game. Please. Solve the tasks the ususal way."} />
      </PageWrapper>
  )
}