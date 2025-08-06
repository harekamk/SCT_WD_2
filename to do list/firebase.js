import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-auth.js";
import { getFirestore, setDoc, doc } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-firestore.js";

const firebaseConfig = {
    apiKey: "AIzaSyCEHP0OeNLmSy2s6PsmAOlgPLLmjcBQlDk",
    authDomain: "login-authenticator-d949b.firebaseapp.com",
    projectId: "login-authenticator-d949b",
    storageBucket: "login-authenticator-d949b.appspot.com",
    messagingSenderId: "570252846584",
    appId: "1:570252846584:web:71295bfe479e4eb5ad620d"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth();
const db = getFirestore();

function showMessage(message, divId) {
    const messageDiv = document.getElementById(divId);
    messageDiv.style.display = "block";
    messageDiv.innerHTML = message;
    messageDiv.style.opacity = 1;
    setTimeout(() => {
        messageDiv.style.opacity = 0;
    }, 5000);
}

const submitSignUp = document.getElementById('submitSignUp');
submitSignUp.addEventListener('click', (event) => {
    event.preventDefault();
    const email = document.getElementById('rEmail').value;
    const password = document.getElementById('rPassword').value;
    const name = document.getElementById('fName').value;

    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            const user = userCredential.user;
            const userData = { email: email, name: name };
            showMessage("Account created successfully!", 'signUpMessage');
            const docRef = doc(db, "users", user.uid);
            setDoc(docRef, userData)
                .then(() => {
                    window.location.href = 'index2.html';
                })
                .catch((error) => {
                    console.error("Error writing document:", error);
                });
        })
        .catch((error) => {
            const errorCode = error.code;
            if (errorCode === 'auth/email-already-in-use') {
                showMessage('Email address already exists!', 'signUpMessage');
            } else {
                showMessage('Unable to create user', 'signUpMessage');
            }
        });
});

const submitSignIn = document.getElementById('submitSignIn');
submitSignIn.addEventListener('click', (event) => {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            showMessage('Login is successful!', 'signInMessage');
            const user = userCredential.user;
            localStorage.setItem('loggedInUserId', user.uid);
            window.location.href = "index2.html";
        })
        .catch((error) => {
            const errorCode = error.code;
            if (errorCode === 'auth/wrong-password' || errorCode === 'auth/user-not-found') {
                showMessage('Incorrect email or password', 'signInMessage');
            } else {
                showMessage('Account does not exist', 'signInMessage');
            }
        });
});