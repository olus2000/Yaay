import React from "react";
import styled from "styled-components";

const StyledRadios = styled.div`
display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
  flex-wrap: wrap;
  height: 150px;
  
`

export const RadioButtons = ({data, name, handler, smol=false}) => {
  return(
      <StyledRadios>
        {data.map((e) => (
            <div style={{display: "flex", width: `${smol ? '30%' : '80%'}`, justifyContent: 'flex-start'}}>
              <input type='radio' value={e} name={name} style={{marginRight: 20}} className={'radioButton'} onClick={() => handler(e)}/>
              <p> {e} </p>
            </div>
        ))}
      </StyledRadios>
  )
}