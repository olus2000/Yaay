import React from "react";
import styled from "styled-components";


const StyledBox = styled.div`
  height: 100px;
  width: 200px;
  position: absolute;
  right: 40px;
  top: 40px;
  display: flex;
  flex-direction: column;
  
  align-items: center;
  
  justify-content: space-evenly;
  
  border-radius: 10px;
  border: 2px dashed black;
  
  .customText {
    margin: 0;
  }

`

export const InfoBox = ({attemptNumber, maxAttempts, taskNumber, maxTasks}) => {

  return (
      <StyledBox>
        <p className={'customText'}>
          {`attempt: ${attemptNumber} / ${maxAttempts}`}
        </p>
        <p className={'customText'}>
          {`task: ${taskNumber} / ${maxTasks}`}
        </p>
      </StyledBox>
  )
}