import React from "react";
import styled from "styled-components";


const StyledButton = styled.button`
  width: 80px;
  height: 30px;
  
  border-radius: 5px;
  border: 2px solid gray;
  transition: 0.3s;

  font-family: 'Cutive Mono', monospace;
  cursor: pointer;
  
  &:hover {
    border: 2px solid black;
    background-color: white;
  }
  
  &:active {
    opacity: 70%;
  }
`

export const AnswerButton = (props) => {

  return(
      <StyledButton onClick={props.onClick}>
        submit
      </StyledButton>
  )
}