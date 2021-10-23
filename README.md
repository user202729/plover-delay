# plover-delay
Plover command plugin to sleep for some time.

See also: [user202729/plover-run-py: Command plugin for Plover to run an arbitrary Python command.](https://github.com/user202729/plover-run-py)

## Usage

In order to use this plugin in [Plover](https://github.com/openstenoproject/plover) you need to
create a dictionary entry of the form:

``` json
{
    "example_stroke": "{PLOVER:DELAY:0.1}"
}
```

`DELAY` can be replaced with `SLEEP` or `WAIT`.

The amount is measured in seconds.

In some new Plover version `{:command:delay:0.1}` would also work.
