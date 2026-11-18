# Project Handoff: Desktop Cat — V1

## 1. Project overview

I want to build a small desktop companion for Windows: a cartoon-style cat that lives on my desktop, preferably in the bottom-right corner.

The goal is not to make another productivity assistant, notification tool, or virtual pet with complicated statistics.

I want a little character that feels like it genuinely lives on my computer.

It should sleep when I'm away, slowly wake up when I return, and have its own collection of activities and behaviours while I'm using my PC.

The experience should feel organic, relaxed, and occasionally amusing.

**Important: We are currently in the planning and specification stage. Do not start coding yet.**

## 2. Core vision

The cat should behave differently depending on the computer's activity.

Its behaviour should not consist of one animation playing continuously. Instead, it should have distinct states, transitions, and a library of possible actions.

The central design principle is:

**Unpredictability within a believable routine.**

Sometimes the cat should do something amusing. Sometimes it should simply sit there. Sometimes it should sleep for a while without doing anything.

It should not feel like a character constantly performing for attention.

## 3. Core behavioural states

### State A: Sleeping

**Trigger:** The PC has been idle for a sufficiently long period, or Windows has resumed from sleep.

Possible behaviours:
- Curl up and sleep.
- Gentle breathing animation.
- Occasional ear twitch.
- Occasional tail movement.
- Remain asleep without unnecessary activity.

The cat should not immediately fall asleep the moment the user stops moving the mouse. There should be an idle threshold and a gradual transition.

### State B: Waking up

**Trigger:** User activity resumes after the cat has fallen asleep.

Possible sequence:
1. Slight movement or stirring.
2. Slowly open its eyes.
3. Look around.
4. Stretch and yawn.
5. Get up and settle into an awake state.

The transition should be gradual rather than instantaneous.

### State C: Awake / Idle

**Trigger:** The PC is being actively used.

Possible behaviours:
- Sit and look around.
- Blink occasionally.
- Move its ears or tail.
- Change sitting or lying positions.
- Groom itself.
- Stretch.
- Occasionally look towards the mouse cursor.

The cat should alternate between these activities with natural pauses.

### State D: Playing / Exploring

This is a collection of occasional autonomous behaviours.

Possible activities:
- Chase its own tail.
- Play with an imaginary object.
- Bat at something with its paw.
- Curiously follow the mouse cursor.
- Look around as though observing its surroundings.
- Move or change its position.
- Perform other small, amusing cat-like activities.

These actions should be selected occasionally, not continuously.

## 4. Computer activity awareness

We need to distinguish between three conditions.

**A. User inactivity**

The PC is still running, but there has been no keyboard or mouse input for a configurable duration.

For initial consideration, an idle threshold of around 3–5 minutes seems reasonable, but this is not finalised.

The cat should gradually become sleepy and eventually fall asleep.

**B. Windows sleep / suspend**

When Windows enters sleep, the application will not continue normal animation.

When the computer resumes, the pet should detect the resume event and begin in its sleeping state. It should then wake up as user activity returns.

**C. Active computer use**

Keyboard or mouse activity resumes. The cat gradually wakes and returns to its awake behaviour.

We should investigate reliable Windows mechanisms for detecting user inactivity and system suspend/resume events during the implementation-planning stage.

## 5. Action library

The cat needs a reusable library of actions.

Initial ideas:

| Category | Actions |
|---|---|
| Idle | Blink, look around, ear twitch |
| Relaxing | Sit, lie down, stretch |
| Grooming | Lick paw, wash face |
| Playing | Chase tail, bat at imaginary objects |
| Curious | Follow mouse, look towards cursor |
| Sleepy | Yawn, curl up, fall asleep |

Each action should ideally have:
- A duration.
- An appropriate entry and exit transition.
- A cooldown to prevent excessive repetition.
- Conditions determining when it can be selected.
- A probability or selection weight.

We should design a system that allows us to add new actions without rewriting the entire behaviour engine.

## 6. Behaviour engine — intended concept

The cat should use a state-based behaviour system.

The broad conceptual flow is:

- Monitor computer activity.
- Determine the cat's current state.
- Check whether a state transition is necessary.
- Select an appropriate action from the current state's action library.
- Play the corresponding animation.
- Wait for the action to finish.
- Select another appropriate action or remain idle.

Transitions should be smooth and contextually appropriate.

For example, the cat should not immediately jump from sleeping to chasing the mouse. It should wake up first.

The exact architecture and implementation are yet to be decided.

## 7. Development workflow

I want to build this incrementally and understand what we're developing.

Please follow this sequence:

### Phase 1 — Behaviour specification
- Finalise the states.
- Define transition conditions.
- Define activity and action libraries.
- Establish timing, cooldowns, and selection rules.
- Consider unusual scenarios and edge cases.

**Deliverable:** A proper V1 behaviour specification.

### Phase 2 — Visual design
- Establish the cat's cartoon appearance.
- Decide proportions, expressions, and general personality.
- Design a consistent character.
- Identify the animations required for each action.
- Plan how animation assets will be created and organised.

**Deliverable:** A consistent character design and animation plan.

### Phase 3 — Animation system
- Implement individual animations.
- Support animation sequencing and transitions.
- Ensure animations can be reused by the behaviour engine.

**Deliverable:** A working library of cat animations.

### Phase 4 — Desktop integration
- Create a transparent, borderless desktop window.
- Position the cat in the bottom-right corner.
- Keep it visible above normal windows.
- Support dragging and repositioning.
- Integrate Windows activity and sleep/resume detection.

**Deliverable:** A functioning desktop companion window.

### Phase 5 — Behaviour engine
- Connect computer activity to the cat's states.
- Implement state transitions.
- Implement autonomous action selection.
- Add cooldowns, timing, and natural pauses.

**Deliverable:** A cat that behaves autonomously.

### Phase 6 — Interaction and polish
- Add mouse interactions.
- Add a context menu and exit mechanism.
- Improve animation transitions.
- Test different screen resolutions.
- Optimise resource usage.
- Consider launching automatically with Windows.
- Package the application as a Windows executable.

**Deliverable:** A polished V1 desktop companion.

## 8. Initial scope boundaries

For V1, focus on:
- One cat.
- One consistent cartoon art style.
- Desktop presence.
- Sleeping and waking.
- Autonomous idle activities.
- A variety of actions and animations.
- Basic user interaction.
- Reliable Windows integration.

Do not introduce these unless we explicitly decide to expand the scope:
- Hunger, energy, or health meters.
- XP, achievements, or levelling.
- Shops, accessories, and inventories.
- Notifications and productivity reminders.
- Voice recognition or conversational AI.
- Complex simulations or unnecessary AI features.

The objective is to make the basic companion feel alive before adding complexity.

## 9. Technical direction

Python is a possible implementation language, but the final technology stack has not been decided.

We should evaluate suitable approaches for:
- Windows desktop overlays.
- Transparent windows.
- Sprite-based or frame-based animation.
- Input inactivity detection.
- System suspend/resume detection.
- Efficient autonomous behaviour.
- Low CPU and memory usage.

Avoid committing to a framework prematurely. Explain the trade-offs before making major technical decisions.

## 10. How I want to collaborate

This is an important part of the project.

I want to build this myself, with Claude acting as a programming partner, technical guide, and reviewer.

Please:
- Work incrementally.
- Prioritise planning and design before implementation.
- Explain architectural decisions and their trade-offs.
- Avoid dumping huge amounts of code.
- Break implementation into understandable components.
- Help me understand the reasoning behind the code.
- Don't introduce unnecessary features or complexity.
- Keep track of decisions already made so we don't repeatedly revisit them.
- Distinguish confirmed requirements from suggestions and unresolved decisions.

Don't rush straight into coding just because the project sounds straightforward.

### Immediate task

Start by reviewing this project brief and helping me refine the **V1 behavioural specification**.

Identify missing decisions, potential edge cases, and design questions.

Let's finalise how the cat should behave before deciding exactly how to implement it.

Do not generate the application code yet.