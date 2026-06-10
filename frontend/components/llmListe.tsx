"use client";

import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Spinner } from "./ui/spinner";

import { useEffect, useState } from "react";

const models = ["gemini-3.5-flash", "Mistral 7b (local)"];

export default function LlmListe() {
  const [selectedValue, setSelectedValue] =
    useState<string>("gemini-3.5-flash");

  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>("");

  const fetchCurrentModel = async () => {
    try {
      setLoading(true);
      setError("");

      const request = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/llm`);

      const response = await request.json();

      if (!request.ok) {
        setError(response.detail || "Failed to load model!");
        return;
      }
      console.log(response);
      if (response.model == "google") {
        setSelectedValue("gemini-3.5-flash");
      } else {
        setSelectedValue("Mistral 7b (local)");
      }
    } catch (err) {
      console.error(err);
      setError("Failed to connect to server!");
    } finally {
      setLoading(false);
    }
  };

  const handleModelChange = async (value: string) => {
    try {
      setLoading(true);
      setError("");

      const request = await fetch(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/llm`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            model_name: value,
          }),
        },
      );

      const response = await request.json();

      if (!request.ok) {
        setError(response.detail || "Failed to change model!");
        return;
      }

      if (response.model == "google") {
        setSelectedValue("gemini-3.5-flash");
      } else {
        setSelectedValue("Mistral 7b (local)");
      }
    } catch (err) {
      console.error(err);
      setError("Failed to connect to server!");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCurrentModel();
  }, []);

  return (
    <div className="flex items-center gap-4">
      {error && <div className="text-red-500 text-sm">{error}</div>}

      <Select
        disabled={loading}
        value={selectedValue}
        onValueChange={handleModelChange}
      >
        <SelectTrigger className="w-45">
          <SelectValue placeholder="Select a model" />
        </SelectTrigger>

        <SelectContent>
          <SelectGroup>
            {models.map((item) => (
              <SelectItem key={item} value={item}>
                {item}
              </SelectItem>
            ))}
          </SelectGroup>
        </SelectContent>
      </Select>

      {loading && <Spinner />}
    </div>
  );
}
