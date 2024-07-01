import React from "react";

const DownloadIcon = ({ color = "white" }: { color?: string }) => {
  return (
    <svg
      width="20"
      height="20"
      viewBox="0 0 20 20"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M15.0259 13.8476L18.5951 17.4159L17.4159 18.5951L13.8476 15.0259C12.5199 16.0903 10.8684 16.6692 9.16675 16.6667C5.02675 16.6667 1.66675 13.3067 1.66675 9.16675C1.66675 5.02675 5.02675 1.66675 9.16675 1.66675C13.3067 1.66675 16.6667 5.02675 16.6667 9.16675C16.6692 10.8684 16.0903 12.5199 15.0259 13.8476ZM13.3542 13.2292C14.4118 12.1417 15.0025 10.6838 15.0001 9.16675C15.0001 5.94425 12.3892 3.33341 9.16675 3.33341C5.94425 3.33341 3.33341 5.94425 3.33341 9.16675C3.33341 12.3892 5.94425 15.0001 9.16675 15.0001C10.6838 15.0025 12.1417 14.4118 13.2292 13.3542L13.3542 13.2292Z"
        fill={color}
      />
    </svg>
  );
};

export default DownloadIcon;