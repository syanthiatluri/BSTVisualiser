async function insert() {
    const values = document.getElementById('values').value.split(',').map(v => parseInt(v.trim()));
    const response = await fetch('/insert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ values: values }),
    });
    const data = await response.json();
    document.getElementById('bst-output').innerHTML = renderTree(data.tree);
}

async function deleteNodes() {
    const values = document.getElementById('delete-values').value.split(',').map(v => parseInt(v.trim()));
    const response = await fetch('/delete', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ values: values }),
    });
    if (response.ok) {
        const data = await response.json();
        document.getElementById('bst-output').innerHTML = renderTree(data.tree);
    } else {
        console.error('Error deleting nodes');
    }
}

function clearAll() {
    document.getElementById('values').value = '';
    document.getElementById('delete-values').value = '';
    document.getElementById('bst-output').innerHTML = '';
}

function renderTree(tree) {
    if (!tree) return '';
    return `
        <div class="tree">
            <div class="node">${tree.key}</div>
            <div class="children">
                <div class="child left">${tree.left ? renderTree(tree.left) : ''}</div>
                <div class="child right">${tree.right ? renderTree(tree.right) : ''}</div>
            </div>
        </div>
    `;
}
