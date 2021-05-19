import React, { useState, useEffect } from "react";
import socketIOClient from "socket.io-client";
const ENDPOINT = "http://127.0.0.1:5000";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    const socket = socketIOClient(ENDPOINT);
    socket.on("message", data => {
      setMessage(data);
    });

    return () => socket.disconnect();
  }, []);

  return (
    <div style={{display: "flex", flexDirection: "row", flexWrap: "wrap"}}>
      <p>
        {message}
      </p>
    </div>
  );
}

export default App;