// Dynamically generate cameras in the grid with a limit of 9 at a time and load more on scroll
window.onload = function() {
    const cameraGrid = document.getElementById('cameraGrid');
    let totalCameras = 50;  
    let camerasPerPage = 9; 
    let camerasDisplayed = 53;

    // Function to load cameras in batches of 9
    function loadCameras() {
        let camerasToLoad = Math.min(totalCameras - camerasDisplayed, camerasPerPage);
        for (let i = 1; i <= camerasToLoad; i++) {
            const cameraDiv = document.createElement('div');
            cameraDiv.classList.add('camera');
            cameraDiv.setAttribute('id', 'camera' + (camerasDisplayed + i));
            cameraDiv.setAttribute('onclick', `openCamera('Camera ${camerasDisplayed + i}')`);
            cameraDiv.innerHTML = `Camera ${camerasDisplayed + i}`;
            cameraGrid.appendChild(cameraDiv);
        }
        camerasDisplayed += camerasToLoad;
    }

    // Initial load of 9 cameras
    loadCameras();

    // Load more cameras when the user scrolls to the bottom of the grid
    cameraGrid.addEventListener('scroll', function() {
        if (cameraGrid.scrollTop + cameraGrid.clientHeight >= cameraGrid.scrollHeight) {
            loadCameras();
        }
    });
};

// Function to open the camera in full screen
function openCamera(cameraName) {
    const modal = document.getElementById('cameraModal');
    const modalContent = document.getElementById('modalCameraContent');
    modal.style.display = 'flex';
    modalContent.innerHTML = `<h2>${cameraName} - Live Stream.....</h2><p>Displaying live stream of ${cameraName}.</p>`;
}

// Function to close the full screen camera view
function closeCamera() {
    const modal = document.getElementById('cameraModal');
    modal.style.display = 'none';
}
