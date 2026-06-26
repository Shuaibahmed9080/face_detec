import WebcamFeed from "@/components/WebcamFeed";

export default function Home() {
  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-5">
        Real Time Face Detection tes
      </h1>

      <WebcamFeed />
    </div>
  );
}