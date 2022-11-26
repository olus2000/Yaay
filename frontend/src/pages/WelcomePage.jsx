import React from "react";
import styled from "styled-components";
import { PageWrapper } from "../utils/PageWrapper";
import { Header } from "../components/header";
import { Task } from "../components/task";


export const WelcomePage = () => {
  return (
      <PageWrapper>
        <Header title={'Welcome!'}/>
        <Task content={"This is a GS secret recruitment boosting site. Find a cryptic looking QR and you might get a chance to join the fun!"} />
      </PageWrapper>
  )
}