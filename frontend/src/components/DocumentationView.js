import React from 'react';

function DocumentationView({ doc }) {
  return (
    <div className="documentation">
      <h2>{doc.filename}</h2>
      <div className="documentation-content">
        {doc.content}
      </div>
    </div>
  );
}

export default DocumentationView;
