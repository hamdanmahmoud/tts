import React, { useEffect, useState } from "react";
const ENDPOINT = "http://127.0.0.1:5000";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    const id = setInterval(() => {
      fetch(ENDPOINT)
      .then(res => res.json())
      .then(res => {
        setMessage('...' + res.message + '...');
      })
      .catch(err => {
        clearInterval(id);
      });
    }, 1000);
  }, [])

  return (
    <div style={{display: "flex", flexDirection: "row", justifyContent: "center", flexWrap: "wrap", margin: "30% 0"}}>
      <div style={{fontSize: "30px", fontWeight: "400", textAlign: "center"}}>
        {message}
      </div>
    </div>
  );
}

export default App;