"use client";

import { useRef, useState } from "react";
import axios from "axios";

export default function WebcamFeed() {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  const [result, setResult] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [name, setName] = useState("");
  const [userId, setUserId] = useState("");
  const [capturedBlob, setCapturedBlob] =
    useState(null);

  // Start camera
  const startCamera = async () => {
    try {
    //   const stream =
    //     await navigator.mediaDevices.getUserMedia({
    //       video: true,
    //     });

    //   videoRef.current.srcObject = stream;
    const stream =
  await navigator.mediaDevices.getUserMedia({
    video: {
      width: 640,
      height: 480,
      facingMode: "user",
    },
  });

if (videoRef.current) {
  videoRef.current.srcObject = stream;
}
    } 
    
    catch (error) {
      console.log(
        "Camera Error:",
        error
      );

      alert(
        "No webcam found or permission denied"
      );
    }
  };

  // Detect face
  const detectFace = async () => {
    const video = videoRef.current;
    const canvas = canvasRef.current;

    if (!video || !canvas) {
      alert("No webcam detected");
      return;
    }

    if (
      video.readyState !== 4 ||
      video.videoWidth === 0
    ) {
      alert("Camera not ready yet");
      return;
    }

    const context =
      canvas.getContext("2d");

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    context.drawImage(video, 0, 0);

    canvas.toBlob(async (blob) => {
      if (!blob) {
        alert("Failed to capture image");
        return;
      }

      const formData = new FormData();

      formData.append(
        "file",
        blob,
        "capture.jpg"
      );

      setCapturedBlob(blob);

      try {
        const res = await axios.post(
          `${process.env.NEXT_PUBLIC_API_URL}/recognize`,
          formData
        );

        setResult(res.data);

        if (!res.data.known) {
          setShowForm(true);
        } else {
          setShowForm(false);
        }
      } catch (error) {
        console.log(error);
      }
    }, "image/jpeg");
  };

  // Register new user
  const registerUser = async () => {
    const formData = new FormData();

    formData.append("name", name);
    formData.append("user_id", userId);

    formData.append(
      "file",
      capturedBlob,
      "capture.jpg"
    );

    try {
      await axios.post(
        `${process.env.NEXT_PUBLIC_API_URL}/register`,
        formData
      );

      alert("User Registered");
      setShowForm(false);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="flex gap-10 items-start p-6">

      {/* Camera Section */}
      <div className="flex flex-col gap-4">

        {/* <video
          ref={videoRef}
          autoPlay
          playsInline
          muted
          className="w-[500px] rounded-lg border"
        /> */}
        <video
  ref={videoRef}
  autoPlay
  playsInline
  muted
  onLoadedMetadata={() =>
    console.log("Camera loaded")
  }
  className="w-[500px] rounded-lg border"
/>

        <canvas
          ref={canvasRef}
          className="hidden"
        />

        <div className="flex gap-4">
          <button
            onClick={startCamera}
            className="bg-blue-500 text-white px-4 py-2 rounded"
          >
            Start Camera
          </button>

          <button
            onClick={detectFace}
            className="bg-green-500 text-white px-4 py-2 rounded"
          >
            Detect Face
          </button>
        </div>

        {/* Recognition Result */}
        {result && (
          <div className="p-4 border rounded-lg">
            <p>
              Status: {result.message}
            </p>
          </div>
        )}
      </div>

      {/* Registration Form */}
      {showForm && (
        <div className="border p-4 rounded-lg w-[300px]">

          <h2 className="text-lg font-bold mb-4">
            Register User
          </h2>

          <input
            type="text"
            placeholder="Name"
            className="border p-2 w-full mb-3"
            onChange={(e) =>
              setName(e.target.value)
            }
          />

          <input
            type="text"
            placeholder="ID"
            className="border p-2 w-full mb-3"
            onChange={(e) =>
              setUserId(e.target.value)
            }
          />

          <button
            onClick={registerUser}
            className="bg-blue-500 text-white px-4 py-2 rounded"
          >
            Register
          </button>
        </div>
      )}
    </div>
  );
}
