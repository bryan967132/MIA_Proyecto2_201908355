import React, { useState } from 'react';
import { MDBContainer, MDBTabs, MDBTabsItem, MDBTabsLink, MDBTabsContent, MDBInput } from 'mdb-react-ui-kit';

export default function Login() {
    const [idPart, setIdPart] = useState('')
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleJustifyClick = () => {
        console.log(idPart, username, password)
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
            </MDBTabsContent>
        </MDBContainer>
    );
}