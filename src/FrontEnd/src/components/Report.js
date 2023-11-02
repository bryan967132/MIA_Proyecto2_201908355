import React, { useState, useEffect } from 'react';
import { API } from './headers.js'
import Popup from "./Popup";
import './Report.css'

export default function Report() {
    const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [message, setMessage] = useState('');
    const [reports, setReports] = useState([]);

    const openPopup = () => {
        setIsPopupOpen(true);
    };

    const closePopup = () => {
        setIsPopupOpen(false);
    };

    const getReports = async () => {
        await fetch(`${API}/getReports`)
        .then(response => response.json())
        .then(response => {
            setReports(response)
        })
        .catch(error => {
            setMessage('Hubo un error al cargar los reportes.')
            openPopup()
        })
    }

    useEffect(() => {
        getReports()
    }, [])

    return (
        <div className="card mt-4">
            <h5 className="card-header">
                <div className='d-flex justify-content-between'>
                    <p>Reportes</p>
                </div>
            </h5>
            <div className="card-body">
                {reports.map((fila, index) => (
                    <div key={index}>
                        <h1>{fila[0]}</h1>
                        <iframe
                            src={fila[1]}
                            title="Página Web"
                            width="100%"
                            height="600"
                        ></iframe>
                    </div>
                ))}
            </div>
            <Popup isOpen={isPopupOpen} onClose={closePopup} message={message}/>
        </div>
    );
}