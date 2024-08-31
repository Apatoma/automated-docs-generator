import React, { useState, useEffect } from 'react';
import Dashboard from './components/Dashboard';
import DocumentationView from './components/DocumentationView';

function App() {
  const [docs, setDocs] = useState([]);
  const [selectedDoc, setSelectedDoc] = useState(null);

  useEffect(() => {
    fetchDocs();
  }, []);

  const fetchDocs = async () => {
    const response = await fetch('http://localhost:5000/docs');
    const data = await response.json();
    setDocs(data);
  };

  const handleDocClick = async (id) => {
    const response = await fetch(`http://localhost:5000/docs/${id}`);
    const data = await response.json();
    setSelectedDoc(data);
  };

  return (
    <div>
      <h1>Automated Documentation Generator</h1>
      <Dashboard docs={docs} onDocClick={handleDocClick} />
      {selectedDoc && <DocumentationView doc={selectedDoc} />}
    </div>
  );
}

export default App;
