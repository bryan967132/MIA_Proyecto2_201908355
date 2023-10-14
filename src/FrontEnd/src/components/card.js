import React, { useState, useRef } from 'react';
import './card.css'
import CodeMirror from '@uiw/react-codemirror';
import { StreamLanguage } from '@codemirror/language';
import { shell } from '@codemirror/legacy-modes/mode/shell';
import { vscodeDark as theme } from '@uiw/codemirror-theme-vscode';
// import { githubDark as theme } from '@uiw/codemirror-theme-github';

export default function Card() {

    const [results, setResults] = useState('');
    const [commands, setCommands] = useState('');
    const [isPaused, setIsPaused] = useState(false);
    const [commands_list, setCommands_list] = useState([]);
    const textAreaRef = useRef(null);
    const API = process.env.REACT_APP_API_URL;

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.onload = (event) => {
            setCommands(event.target.result);
        };
        if (file) {
            reader.readAsText(file);
        }
    };

    const handleTextAreaKeyPress = (event) => {
        if (event.key === 'Enter') {
            if(isPaused) {
                sendCommands(commands_list);
            }
        }
    };

    const sendCommands = async (commands) => {
        for (let i = 0; i < commands.length; i ++) {
            const command = commands[i].trim();
            if (command) {
                setCommands_list(commands.slice(i + 1, commands.length));
                if(command === 'pause') {
                    setIsPaused(true);
                    setResults(prevResults => prevResults + `[Pause] => Presiona Enter para continuar\n`);
                    break;
                }
                try {
                    const response = await fetch(`${API}/parse`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({command}),
                    });
                    const data = await response.json();
                    setResults(prevResults => prevResults + `${data.response}\n`);
                } catch (error) {
                    console.error(`Error en la solicitud ${i + 1}: ${error}`);
                }
            }
        }
    };

    const handleSubmit = () => {
        textAreaRef.current.focus();
        setResults('');
        const commandLines = commands.split('\n');
        setCommands_list(commandLines);
        sendCommands(commandLines);
    };

    const styles = {
        height: 300,
        resize: false,
        color: '#fff',
        backgroundColor: 'rgb(30, 30, 30)',
        fontFamily: 'Consolas',
    }

    const onChange = React.useCallback((value, viewUpdate) => {setCommands(value)}, [])

    return (
        <div className="card mt-4">
            <div className="card-header">
                <div class='columnas'>
                    <div>
                        <button class="send-button" onClick={handleSubmit}>Enviar</button>
                    </div>
                    <div>
                        <input class="form-control" type="file" id="formFile" onChange={handleFileChange}></input>
                    </div>
                </div>
            </div>
            <div className="card-body" class="filas">
                <div>
                    <div class="purple-border">
                        <CodeMirror
                            value={commands}
                            theme={theme}
                            height='300px'
                            extensions={[StreamLanguage.define(shell)]}
                            onChange={onChange}
                            tabSize={10}
                        />
                    </div>
                </div>
                <div class="green-border">
                    <textarea 
                        className="form-control" 
                        placeholder="Resultados" 
                        readOnly
                        ref={textAreaRef}
                        style={styles}
                        value={results}
                        onKeyDown={handleTextAreaKeyPress}
                    />
                </div>
            </div>
        </div>
    );
}