import React from 'react';

function Dashboard({ docs, onDocClick }) {
  return (
    <div className="dashboard">
      <h2>Generated Documentation</h2>
      {docs.length > 0 ? (
        docs.map((doc) => (
          <div key={doc.id} className="doc-item" onClick={() => onDocClick(doc.id)}>
            {doc.filename}
          </div>
        ))
      ) : (
        <p>No documentation available.</p>
      )}
    </div>
  );
}

export default Dashboard;
