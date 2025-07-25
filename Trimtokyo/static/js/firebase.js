// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyA17UQLGwxdPj-o_HeUlNN1TOUiIJEqtbM",
  authDomain: "barber-a7850.firebaseapp.com",
  projectId: "barber-a7850",
  storageBucket: "barber-a7850.firebasestorage.app",
  messagingSenderId: "198586026416",
  appId: "1:198586026416:web:26d8f4d4921b2e02feee75",
  measurementId: "G-GWV62LBT2V"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);


// Initialize Auth service
const auth = firebase.auth();