import Script from "next/script";
import markup from "./original-markup";

export default function Home() {
  return (
    <>
      {/* display:contents => wrapper box layout me koi farq nahi daalta, DOM original jaisa behave karta hai */}
      <div style={{ display: "contents" }} dangerouslySetInnerHTML={{ __html: markup }} />
      <Script src="/app.js" strategy="afterInteractive" />
    </>
  );
}
