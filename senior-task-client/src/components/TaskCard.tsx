import React from "react";
import type { Task, Priority } from "../types";

interface TaskCardProps {
  task: Task;
  onStatusChange?: (id: number, status: Task["status"]) => void;
  className?: string;
}

const priorityStyles: Record<Priority, string> = {
  low: "bg-slate-100 text-slate-700 border-slate-200",
  medium: "bg-blue-50 text-blue-700 border-blue-200",
  high: "bg-amber-50 text-amber-700 border-amber-200",
  critical: "bg-red-50 text-red-700 border-red-200",
};

export const TaskCard: React.FC<TaskCardProps> = ({
  task,
  onStatusChange,
  className = "",
}) => {
  return (
    <article
      className={`rounded-lg border p-4 shadow-sm transition hover:shadow-md ${priorityStyles[task.priority]} ${className}`}
      data-testid="task-card"
    >
      <header className="flex items-start justify-between gap-2">
        <h3 className="text-lg font-semibold leading-tight">{task.title}</h3>
        <span className="shrink-0 rounded-full bg-white/70 px-2 py-0.5 text-xs font-medium uppercase tracking-wide">
          {task.priority}
        </span>
      </header>

      {task.description && (
        <p className="mt-2 text-sm opacity-80">{task.description}</p>
      )}

      <footer className="mt-3 flex items-center justify-between text-xs">
        <span className="rounded bg-white/60 px-2 py-1 font-medium">
          {task.status.replace("_", " ")}
        </span>
        {onStatusChange && (
          <button
            type="button"
            className="rounded bg-white px-2 py-1 text-xs font-medium shadow-sm hover:bg-white/80"
            onClick={() =>
              onStatusChange(
                task.id,
                task.status === "todo" ? "in_progress" : "done"
              )
            }
          >
            Advance
          </button>
        )}
      </footer>
    </article>
  );
};
