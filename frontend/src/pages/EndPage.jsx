import React from 'react';
import { useParams } from "react-router-dom";
import {PageWrapper} from "../utils/PageWrapper";
import {Header} from "../components/header";
import {Task} from "../components/task";
import {handleEndGet} from "../api/endApi";
import {ErrorPage} from "../components/errorPage";
import QRCode from "qrcode.react";
import styled from "styled-components";
import { Survey } from "../components/survey";


const StyledQR = styled.div`
  position: absolute;
  left: 250px;
  display: flex;
  flex-direction: column;
  align-items: center;
  
  .DownloadButton {
    width: 150px;
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
  }
`

export const EndPage = () => {
  const [data, setData] = React.useState(null)
  const userId = useParams().id

  React.useEffect(() => {
    data === null && handleEndGet(setData, userId)
  })

  const explain = "You completed the Goldman Sachs secret challenge!"

  const prompt = "Download the QR code below and use it at the Job Fair to get your prize!";
  if (data === 'error')
    return(
        <ErrorPage />
    )

  const downloadQR = () => {
    const canvas = document.getElementById("qr");
    const pngUrl = canvas
        .toDataURL("image/png")
        .replace("image/png", "image/octet-stream");
    let downloadLink = document.createElement("a");
    downloadLink.href = pngUrl;
    downloadLink.download = "GoldmanSachsPrize.png";
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
  };


  if (data !== null)
  return(
      <PageWrapper>
        <Survey />
        <Header title={'Congratulations!'} />
        <Task content={data} />
        <Task content={explain} />
        <a href={'https://www.goldmansachs.com'} style={{fontSize: 14, marginLeft: 20}} target={'_blank'}> Lear about us here </a>
        <Task content={prompt} />
        <StyledQR>
        <QRCode
            id='qr'
            value={userId}
            size={300}
            level={"L"}
            bgColor={'#e8e6c3'}
            includeMargin={true}
        />
        <button onClick={downloadQR} className={'DownloadButton'}>
          Download QR
        </button>
        </StyledQR>
      </PageWrapper>
  )

  return(
      <div />
  )
}