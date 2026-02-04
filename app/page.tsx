"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import {
  ComposableMap,
  Geographies,
  Geography,
  Marker,
  ZoomableGroup
} from "react-simple-maps";

type GeoPoint = {
  lat: number;
  lng: number;
  zoom: number;
};

type ChallengePayload = {
  id: string;
  title: string;
  prompt: string;
  answer: string;
  hints: string[];
  type: string;
  fun_fact: string;
  location: GeoPoint | null;
};

type GeoFunResponse = {
  challenge: ChallengePayload;
  world_fact: string;
  inspiration: string;
  generated_at: string;
};

const MAP_RESOURCE = "/world-110m.json";

export default function Page() {
  const [data, setData] = useState<GeoFunResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [showAnswer, setShowAnswer] = useState<boolean>(false);

  const fetchChallenge = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      setShowAnswer(false);
      const response = await fetch("/api/geo_fun");
      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }
      const payload: GeoFunResponse = await response.json();
      setData(payload);
    } catch (fetchError) {
      setError(
        fetchError instanceof Error
          ? fetchError.message
          : "Unable to fetch geography fun right now."
      );
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    void fetchChallenge();
  }, [fetchChallenge]);

  const formattedTimestamp = useMemo(() => {
    if (!data) return "";
    const stamp = new Date(data.generated_at);
    return stamp.toLocaleString(undefined, {
      hour: "numeric",
      minute: "2-digit",
      second: "2-digit",
      hour12: true
    });
  }, [data]);

  return (
    <main className="app-shell">
      <section className="panel">
        <span className="tag-pulse">Live cartography playground</span>
        <div className="challenge-card">
          <h1>Geographer Fun Lab</h1>
          <p className="lead">
            Explore a rotating supply of geo trivia, carto puzzles, and map
            storytelling prompts. Each card is brewed by a playful Python
            microservice that loves the planet as much as you do.
          </p>
          <button
            className="primary-btn"
            type="button"
            onClick={() => void fetchChallenge()}
            disabled={loading}
          >
            {loading ? "Mixing a new map..." : "New Geography Challenge"}
          </button>
          {loading && <div className="loading-state">Summoning world data...</div>}
          {error && <div className="error-state">{error}</div>}
          {!loading && !error && data && (
            <>
              <div className="challenge-type">{data.challenge.type}</div>
              <div className="challenge-prompt">{data.challenge.prompt}</div>
              <div className="hint-stack">
                <h3>Field Notes</h3>
                <ul>
                  {data.challenge.hints.map((hint, idx) => (
                    <li key={`${data.challenge.id}-hint-${idx}`}>{hint}</li>
                  ))}
                </ul>
              </div>
              <div className="answer-block">
                <div className="answer-text">
                  {showAnswer ? (
                    <>
                      <strong>Answer:</strong> {data.challenge.answer}
                    </>
                  ) : (
                    <span className="hidden-text">???</span>
                  )}
                </div>
                <button
                  className="primary-btn"
                  type="button"
                  onClick={() => setShowAnswer((prev) => !prev)}
                >
                  {showAnswer ? "Hide Answer" : "Reveal Answer"}
                </button>
              </div>
              <div className="fact-card">
                <strong>Fun Fact:</strong> {data.challenge.fun_fact}
              </div>
            </>
          )}
        </div>
      </section>

      <section className="panel map-panel">
        <h2>
          Atlas View
          <span className="status-chip">
            {formattedTimestamp ? `Updated ${formattedTimestamp}` : "Loading"}
          </span>
        </h2>
        <div className="map-wrapper">
          <ComposableMap projectionConfig={{ scale: 150 }}>
            <ZoomableGroup
              zoom={Math.min(
                Math.max(data?.challenge.location?.zoom ?? 1.4, 1),
                8
              )}
              center={
                data?.challenge.location
                  ? [
                      data.challenge.location.lng,
                      data.challenge.location.lat
                    ]
                  : [0, 20]
              }
              translateExtent={[
                [-1000, -500],
                [1000, 500]
              ]}
            >
              <Geographies geography={MAP_RESOURCE}>
                {({ geographies }) =>
                  geographies.map((geo) => (
                    <Geography
                      key={geo.rsmKey}
                      geography={geo}
                      style={{
                        default: {
                          fill: "rgba(148, 163, 184, 0.35)",
                          outline: "none"
                        },
                        hover: {
                          fill: "rgba(94, 234, 212, 0.55)",
                          outline: "none"
                        },
                        pressed: {
                          fill: "rgba(56, 189, 248, 0.55)",
                          outline: "none"
                        }
                      }}
                    />
                  ))
                }
              </Geographies>
              {data?.challenge.location && (
                <Marker
                  coordinates={[
                    data.challenge.location.lng,
                    data.challenge.location.lat
                  ]}
                >
                  <g transform="translate(0, -12)">
                    <circle r={5} fill="#facc15" opacity={0.95} />
                    <circle r={11} fill="rgba(250, 204, 21, 0.35)" />
                  </g>
                </Marker>
              )}
            </ZoomableGroup>
          </ComposableMap>
        </div>
        {!loading && !error && data && (
          <>
            <div className="fact-card">
              <strong>World Whisper:</strong> {data.world_fact}
            </div>
            <div className="fact-card">
              <strong>Cartography Prompt:</strong> {data.inspiration}
            </div>
          </>
        )}
      </section>
    </main>
  );
}
