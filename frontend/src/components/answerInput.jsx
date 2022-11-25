import React from "react";
import styled from "styled-components";


const StyledInput = styled.input`
  width: 200px;
  margin-left: 40px;
  height: 20px;
  font-family: 'Cutive Mono', monospace;
  transition: 0.3s;
  border: 2px solid gray;
  border-radius: 5px;

  
  &:focus {
    outline: none;
    border: 2px solid black;
  }
`

export const AnswerInput = (props) => {

  return (
      <StyledInput onChange={props.onChange} />
  )
}