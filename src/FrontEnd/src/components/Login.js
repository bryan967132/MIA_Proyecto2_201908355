import React, { useState } from 'react';
import { headers, API } from './headers.js'
import { MDBContainer, MDBTabs, MDBTabsItem, MDBTabsLink, MDBTabsContent, MDBInput } from 'mdb-react-ui-kit';
import Popup from "./Popup";

export default function Login({setActiveOption}) {
    const [idPart, setIdPart] = useState('')
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [message, setMessage] = useState('');

    const openPopup = () => {
        setIsPopupOpen(true);
    };

    const closePopup = () => {
        setIsPopupOpen(false);
    };

    const handleJustifyClick = async () => {
        var msg = ''
        if(idPart === '') {
            msg += 'No ingresó ID de la partición montada'
        }
        if(username === '') {
            msg += (msg !== '' ? '\n' : '') + 'No ingresó Nombre de Usuario'
        }
        if(password === '') {
            msg += (msg !== '' ? '\n' : '') + 'No ingresó Contraseña'
        }
        if(msg !== '') {
            setMessage(msg)
            openPopup()
            return
        }
        await fetch(`${API}/parse`, {
            method: 'POST',
            headers,
            body: JSON.stringify({command: `login -user=${username} -pass=${password} -id=${idPart}`, 'line': 1}),
        })
        .then(response => response.json())
        .then(response => {
            if(response.response === ` -> login: Sesión iniciada exitosamente. (${username}) [1:1]`) {
                setActiveOption('Reportes')
            } else {
                setMessage('Verifique sus credenciales.')
                openPopup()
            }
        })
        .catch(error => {
            setMessage('Hubo un error al iniciar sesión.')
            openPopup()
        })
    };

    return (
        <MDBContainer className="p-3 my-5 d-flex flex-column w-50">
            <MDBTabsContent>
                <div className="text-center">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/lotus.webp"
                        style={{width: '185px'}} alt="logo" />
                    <h4 className="mt-1 mb-5 pb-1">Login</h4>
                </div>
                <MDBInput
                    wrapperClass='mb-4'
                    label='ID Partición'
                    id='fieldID'
                    type='text'
                    value={idPart}
                    onChange={(e) => setIdPart(e.target.value)}
                />
                <MDBInput
                    wrapperClass='mb-4'
                    label='Usuario'
                    id='fieldUsername'
                    type='text'
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <MDBInput
                    wrapperClass='mb-4'
                    label='Contraseña'
                    id='fieldPassword'
                    type='password'
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <MDBTabs pills justify className='mb-3 d-flex flex-row justify-content-between'>
                    <MDBTabsItem>
                        <MDBTabsLink onClick={() => handleJustifyClick()} active={true}>
                            Login
                        </MDBTabsLink>
                    </MDBTabsItem>
                </MDBTabs>
                <Popup isOpen={isPopupOpen} onClose={closePopup} message={message}/>
            </MDBTabsContent>
        </MDBContainer>
    );
}