import React from "react";
import styled from "styled-components";

const StyledHeader = styled.p`
  font-size: 40px;
  align-self: center;
  margin: 30px;
`




export const Header = (props) => {
  return (
    <StyledHeader>
      {props.title}
    </StyledHeader>
  )
}