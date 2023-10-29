import React, { useState } from "react";
import 'bootstrap/dist/css/bootstrap.min.css'
import Navbar from './components/navbar'
import Card from './components/card';
import Login from './components/Login';

export default function App() {
    const [state, setState] = useState({activeOption: 'Consola'})

    const setActiveOption = (option) => {
        setState({ activeOption: option });
    };

    return (
        <div>
            <Navbar setActiveOption={setActiveOption}/>
            <div className='container' style={{padding: "20px", alignItems: 'center'}}>
                {
                    state.activeOption === "Consola" ?
                        <Card/>
                    : state.activeOption === "Login" ?
                        <Login/>
                    :
                        <div>Contenido de Reportes</div>
                }
            </div>
        </div>
    );
}