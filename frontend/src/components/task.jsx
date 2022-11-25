import React from "react";
import styled from "styled-components";

const StyledTask = styled.div`
  margin-left: 20px;
  margin-top: 40px;
  
  max-width: 900px;
  
  content: {
    font-size: 14px;
    justify-content: center;
    align-content: center;
  }

`



export const Task = (props) => {

  return (
      <StyledTask>
        <p className={'content'}>
          {props.content}
        </p>
      </StyledTask>
  )
}