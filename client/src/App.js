import React, { useEffect, useState } from "react";
import './App.scss';

const ENDPOINT = "http://127.0.0.1:5000";

function App() {
  const [oldSpeech, setOldSpeech] = useState("");
  const [newSpeech, setNewSpeech] = useState("");
  const [source, setSource] = useState(undefined);
  const [target, setTarget] = useState(undefined);

  useEffect(() => {
    const id = setInterval(() => {
      fetch(ENDPOINT)
      .then(res => res.json())
      .then(res => {
        const {oldSpeech, newSpeech, source, target} = res;
        setOldSpeech(`...${oldSpeech}`);
        setNewSpeech(` ${newSpeech}...`);
        setSource(source);
        setTarget(target);
      })
      .catch(err => {
        clearInterval(id);
      });
    }, 2000);
  }, [])

  return (
    <div style={{display: "flex", flexDirection: "column", justifyContent: "center", flexWrap: "wrap", margin: "10% 0"}}>
      <div style={{fontSize: "60px", textAlign: "center", color: "white", fontFamily: "serif"}}>
        Live speech
      </div>
      <div style={{fontSize: "25px", textAlign: "center", color: "#092a2e"}}>
        real-time translator
      </div>
      <div style={{display: 'flex', flexDirection:'row', justifyContent: "center", alignContent: "center", fontSize: "25px", fontWeight: "400", textAlign: "center", marginTop: "10rem", color: "white"}}>
        <div style={{margin: '0 0.5rem'}}>{oldSpeech}</div>
        <div style={{color: 'red', fontWeight: '600'}}>{newSpeech}</div>
      </div>
      <div style={{display: "flex", flexDirection: "row", justifyContent: "space-between", margin: "10rem 40rem", alignItems: "center", color: "white", fontWeight: "500"}}>
        <div className={`flag flag-${source}`}/>
        TO
        <div className={`flag flag-${target}`}/>
      </div>
    </div>
  );
}

export default App;