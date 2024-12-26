---
title: "{{ dateFormat "January" (now.AddDate 0 1 0) }} {{ dateFormat "2006" .Date }} Meetup"
description: "description"
date: "{{ dateFormat "2006-01-02" .Date }}"
draft: true
tags:
  - "golang"
---
{{< description >}}

Meetup #00 {{< meetdate >}}. Please RSVP as [Meetup](https://meetup.com)

We will be meeting online using this [Online Meeting](https://meet.jit.si/moderated/faf57089abb075e1133167ba9129db0f31ee7d315de64ad5e9e152aabd2276f7) at 6:30pm MST.

## Agenda

### Talk

Talk description

## News

- News

## Events

- Edmonton Go - [{{ dateFormat "January" (now.AddDate 0 2 0) }}](/meetup/{{ dateFormat "2006-01" (now.AddDate 0 2 0) }}/)
