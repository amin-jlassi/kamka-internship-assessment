"use client";

import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { useState } from "react";

const models = ["gemini-3.5-flash", "Mistral 7b (local)"];

export default function LlmListe() {
  const [selectedValue, setSelectedValue] = useState("gemini-3.5-flash");

  return (
    <Select 
      value={selectedValue}           
      onValueChange={setSelectedValue}
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
  );
}
