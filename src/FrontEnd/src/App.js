import React, { useState } from "react";
import 'bootstrap/dist/css/bootstrap.min.css'
import { API } from './components/headers.js'
import Navbar from './components/navbar'
import Card from './components/Card.js';
import Login from './components/Login';
import Report from './components/Report'

export default function App() {
    const [state, setState] = useState({activeOption: 'Consola'})

    const setActiveOption = async (option) => {
        if(option !== 'Consola')  {
            option = await validateLogged(option)
        }
        setState({ activeOption: option });
    };

    const validateLogged = async (option) => {
        await fetch(`${API}/isLogged`)
        .then(response => response.json())
        .then(response => {
            if(!response.isLogged) {
                option = 'Login'
            } else {
                option = 'Reportes'
            }
        })
        .catch(error => {})
        return option
    }

    return (
        <div>
            <Navbar setActiveOption={setActiveOption}/>
            <div className='container' style={{padding: "20px", alignItems: 'center'}}>
                {
                    state.activeOption === "Consola" ?
                        <Card/>
                    : state.activeOption === "Login" ?
                        <Login setActiveOption={setActiveOption}/>
                    :
                        <Report/>
                }
            </div>
        </div>
    );
}